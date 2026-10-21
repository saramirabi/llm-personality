"""Load p2_prompts_v1.yaml and assemble system and user messages."""

from __future__ import annotations

from pathlib import Path

CONDITIONS = ("P0", "P1", "P2", "P3", "P4", "P5")


def _dedent_block(lines: list[str]) -> str:
    if not lines:
        return ""
    indents = [len(line) - len(line.lstrip(" ")) for line in lines if line.strip()]
    trim = min(indents) if indents else 0
    return "\n".join(line[trim:] if len(line) >= trim else line.lstrip(" ") for line in lines)


def load_prompt_file(path: Path) -> dict[str, object]:
    """Load the study prompt YAML. The file is small and uses only block scalars, quotes, and null."""
    lines = path.read_text(encoding="utf-8").splitlines()
    base_system = _read_block(lines, "base_system")
    header_line = _find_key_line(lines, "persona_header")
    persona_header = _parse_scalar(header_line.split(":", 1)[1].strip())
    if not isinstance(persona_header, str):
        raise ValueError("persona_header must be a string.")
    personas: dict[str, str | None] = {}
    for condition in CONDITIONS:
        personas[condition] = _read_persona(lines, condition)
    user_template = _read_block(lines, "user_template")
    if "{context}" not in user_template:
        raise ValueError("user_template is missing {context}.")
    return {
        "base_system": base_system,
        "persona_header": persona_header,
        "personas": personas,
        "user_template": user_template,
    }


def _find_key_line(lines: list[str], key: str) -> str:
    prefix = f"{key}:"
    for line in lines:
        if line.startswith(prefix):
            return line
    raise ValueError(f"Missing key {key}.")


def _parse_scalar(raw: str) -> str | None:
    if raw == "null":
        return None
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in {'"', "'"}:
        return raw[1:-1]
    return raw


def _read_block(lines: list[str], key: str) -> str:
    start = None
    for index, line in enumerate(lines):
        if line.startswith(f"{key}:"):
            start = index
            break
    if start is None:
        raise ValueError(f"Missing block {key}.")
    if lines[start].split(":", 1)[1].strip() != "|":
        raise ValueError(f"{key} must be a literal block.")
    block: list[str] = []
    for line in lines[start + 1 :]:
        if line and not line.startswith(" "):
            break
        block.append(line)
    text = _dedent_block(block)
    if text and not text.endswith("\n"):
        text += "\n"
    return text


def _read_persona(lines: list[str], condition: str) -> str | None:
    prefix = f"  {condition}:"
    start = None
    for index, line in enumerate(lines):
        if line.startswith(prefix):
            start = index
            break
    if start is None:
        raise ValueError(f"Missing persona {condition}.")
    rest = lines[start].split(":", 1)[1].strip()
    if rest == "null":
        return None
    if rest != "|":
        raise ValueError(f"Persona {condition} must be null or a literal block.")
    block: list[str] = []
    for line in lines[start + 1 :]:
        if line.strip() == "" or line.startswith("    "):
            block.append(line)
            continue
        break
    text = _dedent_block(block)
    if text and not text.endswith("\n"):
        text += "\n"
    return text


def assemble_system(prompts: dict[str, object], condition: str) -> str:
    base_system = str(prompts["base_system"])
    personas = prompts["personas"]
    if not isinstance(personas, dict) or condition not in personas:
        raise ValueError(f"Unknown condition {condition}.")
    persona = personas[condition]
    if persona is None:
        return base_system
    header = str(prompts["persona_header"])
    return f"{base_system}\n{header}\n{persona}"


def assemble_user(prompts: dict[str, object], context: str) -> str:
    template = str(prompts["user_template"])
    return template.replace("{context}", context)
