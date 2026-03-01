#!/usr/bin/env python3
"""
MAAS Documentation — Diagram Generator

Gerador AUTOMÁTICO de diagramas Mermaid para documentação MAAS.

Funcionalidades:
- generate_dag(): Diagrama de fluxo de átomos (Estado A → Átomos → Estado B)
- generate_atom_structure(): Estrutura Input/Decisão/Output/Fricção
- generate_agent_matrix(): Matriz visual de alocação de agentes
- generate_ke_equation(): Equação Ke como diagrama
- generate_four_causes(): 4 Causas aristotélicas

Usage:
    from scripts.generate-diagrams import *

    atoms = [
        {"id": "a1", "name": "Extrair decisões", "input": "Expert", "output": "Lista"},
    ]

    dag = generate_dag(atoms, "Input", "Output")
    print(dag)

Author: MAAS Skill
Version: 1.0.0
"""

from typing import List, Dict, Optional
import json


def generate_dag(atoms: List[Dict], state_a: str = "ESTADO A",
                 state_b: str = "ESTADO B", style: str = "maas") -> str:
    """
    Gera diagrama de fluxo (DAG) dos átomos.

    Args:
        atoms: Lista de átomos com keys: id, name, input, output
        state_a: Nome do estado inicial
        state_b: Nome do estado final
        style: Estilo do diagrama ('maas', 'simple', 'detailed')

    Returns:
        Código Mermaid para o diagrama

    Example:
        atoms = [
            {"id": "a1", "name": "Extrair decisões", "input": "Expert", "output": "Lista"},
            {"id": "a2", "name": "Atomizar", "input": "Lista", "output": "Átomos docs"},
        ]
        dag = generate_dag(atoms, "Input", "Output")
    """
    mermaid = ["graph TD"]

    # Define styles based on style parameter
    styles = _get_dag_styles(style)

    # Add state definitions
    mermaid.append(f"    A[{state_a}]")
    mermaid.append(f"    B[{state_b}]")

    # Add atom definitions
    for atom in atoms:
        node_id = atom.get("id", f"atom_{atoms.index(atom)}")
        node_label = atom.get("name", "Átomo")
        mermaid.append(f"    {node_id}[{node_label}]")

    # Add connections
    if atoms:
        # State A to first atom
        mermaid.append(f"    A --> {atoms[0].get('id', 'atom_0')}")

        # Atoms to each other
        for i in range(len(atoms) - 1):
            current = atoms[i].get("id", f"atom_{i}")
            next_atom = atoms[i + 1].get("id", f"atom_{i + 1}")
            mermaid.append(f"    {current} --> {next_atom}")

        # Last atom to State B
        mermaid.append(f"    {atoms[-1].get('id', f'atom_{len(atoms)-1}')} --> B")

    # Add styling
    mermaid.append("")
    mermaid.append("    " + "\n    ".join(styles))

    return "\n".join(mermaid)


def _get_dag_styles(style: str) -> List[str]:
    """Retorna estilos CSS para o DAG baseado no estilo escolhido."""
    if style == "maas":
        return [
            "style A fill:#e1f5ff stroke:#0288d1",
            "style B fill:#c8e6c9 stroke:#388e3c",
            "style A1 fill:#fff9c4 stroke:#fbc02d",
            "style A2 fill:#fff9c4 stroke:#fbc02d",
            "style A3 fill:#fff9c4 stroke:#fbc02d",
            "style A4 fill:#fff9c4 stroke:#fbc02d",
            "style A5 fill:#fff9c4 stroke:#fbc02d",
        ]
    elif style == "simple":
        return [
            "style A fill:#e3f2fd",
            "style B fill:#c8e6c9",
        ]
    else:  # detailed
        return [
            "classDef start fill:#e1f5ff,stroke:#0288d1,stroke-width:2px",
            "classDef end fill:#c8e6c9,stroke:#388e3c,stroke-width:2px",
            "classDef atom fill:#fff9c4,stroke:#fbc02d,stroke-width:2px",
            "class A start",
            "class B end",
        ]


def generate_atom_structure(atom: Dict, include_friction: bool = True) -> str:
    """
    Gera diagrama da estrutura de um átomo.

    Args:
        atom: Dicionário com keys: input, decision, output, friction
        include_friction: Incluir fricção no diagrama

    Returns:
        Código Mermaid para o diagrama

    Example:
        atom = {
            "input": "CRM do cliente",
            "decision": "Analisar histórico de compras",
            "output": "Lista de categorias",
            "friction": "Cognitiva"
        }
        diag = generate_atom_structure(atom)
    """
    mermaid = ["graph LR"]

    # Define nodes
    input_text = atom.get("input", "INPUT")
    decision_text = atom.get("decision", "DECISÃO")
    output_text = atom.get("output", "OUTPUT")

    mermaid.append(f"    I[📥 {input_text}]")
    mermaid.append(f"    D{{⚙️ {decision_text}}}")
    mermaid.append(f"    O[📤 {output_text}]")

    # Define connections
    mermaid.append("    I --> D")
    mermaid.append("    D --> O")

    # Add friction if included
    if include_friction and atom.get("friction"):
        friction = atom.get("friction")
        mermaid.append(f"    F[⚠️ {friction}]")
        mermaid.append("    F -.bloqueia.-> D")
        mermaid.append("")
        mermaid.append("    style F fill:#ffcdd2,stroke:#c62828")

    # Add styling
    mermaid.append("")
    mermaid.append("    style I fill:#e3f2fd,stroke:#0288d1")
    mermaid.append("    style D fill:#fff9c4,stroke:#fbc02d")
    mermaid.append("    style O fill:#c8e6c9,stroke:#388e3c")

    return "\n".join(mermaid)


def generate_agent_matrix(atoms: List[Dict], agents: Optional[Dict] = None) -> str:
    """
    Gera diagrama da matriz de alocação de agentes.

    Args:
        atoms: Lista de átomos com keys: id, name, agent
        agents: Dicionário opcional {agent_type: [atom_ids]}

    Returns:
        Código Mermaid para o diagrama

    Example:
        atoms = [
            {"id": "a1", "name": "Atom 1", "agent": "SISTEMA"},
            {"id": "a2", "name": "Atom 2", "agent": "IA"},
        ]
        matrix = generate_agent_matrix(atoms)
    """
    mermaid = ["graph TB"]

    # Build agent groups if not provided
    if agents is None:
        agents = {}
        for atom in atoms:
            agent_type = atom.get("agent", "SISTEMA")
            if agent_type not in agents:
                agents[agent_type] = []
            agents[agent_type].append(atom.get("id", atom.get("name", "?")))

    # Agent type colors
    agent_colors = {
        "SISTEMA": "#90caf9",
        "IA": "#ce93d8",
        "IA autônoma": "#ce93d8",
        "IA + Humano": "#b39ddb",
        "Humano + IA": "#b39ddb",
        "Humano": "#ef9a9a",
        "UI/UX": "#ffcc80",
    }

    # Create subgraphs for each agent type
    for agent_type, atom_list in agents.items():
        # Sanitize subgraph name (Mermaid doesn't like special chars)
        safe_name = agent_type.replace(" ", "_").replace("+", "plus")
        color = agent_colors.get(agent_type, "#e0e0e0")

        mermaid.append(f"    subgraph {safe_name}[🔧 {agent_type}]")
        for atom_id in atom_list:
            mermaid.append(f"        {atom_id}[{atom_id}]")
        mermaid.append(f"    end")
        mermaid.append(f"    style {safe_name} fill:{color}20,stroke:{color}")

        # Add spacing
        mermaid.append("")

    return "\n".join(mermaid)


def generate_ke_equation(ke_vars: Optional[Dict] = None) -> str:
    """
    Gera diagrama da Equação Ke.

    Args:
        ke_vars: Dicionário opcional com valores de T, A, M, Amp, Lc

    Returns:
        Código Mermaid para o diagrama

    Example:
        ke_vars = {"T": 0.8, "A": 0.9, "M": 0.85, "Amp": 10, "Lc": 0.3}
        eq = generate_ke_equation(ke_vars)
    """
    mermaid = ["graph LR"]
    mermaid.append("    direction TB")

    # Define nodes with values if provided
    if ke_vars:
        t_val = ke_vars.get("T", "T")
        a_val = ke_vars.get("A", "A")
        m_val = ke_vars.get("M", "M")
        amp_val = ke_vars.get("Amp", "Amp")
        lc_val = ke_vars.get("Lc", "Lc")
    else:
        t_val = "T"
        a_val = "A"
        m_val = "M"
        amp_val = "Amp"
        lc_val = "Lc"

    mermaid.append(f"    T[Transferibilidade<br/>T={t_val}]")
    mermaid.append(f"    A[Aplicabilidade<br/>A={a_val}]")
    mermaid.append(f"    M[Metodização<br/>M={m_val}]")
    mermaid.append(f"    Amp[Amplificador IA<br/>Amp={amp_val}×]")
    mermaid.append(f"    Lc[Limite Cognitivo<br/>Lc={lc_val}]")

    # Multiplication nodes
    mermaid.append("    M1((×))")
    mermaid.append("    M2((×))")
    mermaid.append("    M3((×))")
    mermaid.append("    D((÷))")

    # Result node
    mermaid.append("    Ke[💡 Ke]")

    # Connections - numerator
    mermaid.append("    T --> M1")
    mermaid.append("    A --> M1")
    mermaid.append("    M1 --> M2")
    mermaid.append("    M --> M2")
    mermaid.append("    M2 --> M3")
    mermaid.append("    Amp --> M3")

    # Division
    mermaid.append("    M3 --> D")
    mermaid.append("    Lc --> D")
    mermaid.append("    D --> Ke")

    # Styling
    mermaid.append("")
    mermaid.append("    style T fill:#c8e6c9,stroke:#388e3c")
    mermaid.append("    style A fill:#c8e6c9,stroke:#388e3c")
    mermaid.append("    style M fill:#c8e6c9,stroke:#388e3c")
    mermaid.append("    style Amp fill:#ce93d8,stroke:#8e24aa")
    mermaid.append("    style Lc fill:#ffcdd2,stroke:#c62828")
    mermaid.append("    style Ke fill:#fff9c4,stroke:#fbc02d,stroke-width:3px")
    mermaid.append("    style M1 fill:#e3f2fd,stroke:#0288d1")
    mermaid.append("    style M2 fill:#e3f2fd,stroke:#0288d1")
    mermaid.append("    style M3 fill:#e3f2fd,stroke:#0288d1")
    mermaid.append("    style D fill:#e3f2fd,stroke:#0288d1")

    return "\n".join(mermaid)


def generate_four_causes() -> str:
    """
    Gera diagrama das 4 Causas aristotélicas.

    Returns:
        Código Mermaid para o diagrama
    """
    mermaid = ["graph TD"]
    mermaid.append("    direction TB")

    mermaid.append("    title[As 4 Causas de Metodologia]")
    mermaid.append("    title --> M[Material<br/>📦 DECISÕES SEQUENCIADAS]")
    mermaid.append("    title --> F[Formal<br/>🏗️ INPUT → TRANSFORMAÇÃO → OUTPUT]")
    mermaid.append("    title --> E[Eficiente<br/>⚙️ O AGENTE QUE EXECUTA]")
    mermaid.append("    title --> FI[Final<br/>🎯 REDUZIR FRICÇÃO A → B]")

    # Add styling
    mermaid.append("")
    mermaid.append("    style title fill:#e3f2fd,stroke:#0288d1,stroke-width:3px")
    mermaid.append("    style M fill:#fff9c4,stroke:#fbc02d")
    mermaid.append("    style F fill:#fff9c4,stroke:#fbc02d")
    mermaid.append("    style E fill:#fff9c4,stroke:#fbc02d")
    mermaid.append("    style FI fill:#c8e6c9,stroke:#388e3c")

    return "\n".join(mermaid)


def generate_anatomy_diagram() -> str:
    """
    Gera diagrama da Anatomia de Metodologia (5 Partes).

    Returns:
        Código Mermaid para o diagrama
    """
    mermaid = ["graph TD"]
    mermaid.append("    direction TB")

    mermaid.append("    A[ESTADO A<br/>Ponto de Partida]")
    mermaid.append("    T[TRANSFORMAÇÕES<br/>Os Átomos de Decisão]")
    mermaid.append("    B[ESTADO B<br/>Ponto de Chegada]")
    mermaid.append("    F[FRIÇÕES<br/>O que Impede]")
    mermaid.append("    AG[AGENTES<br/>Quem Executa]")

    mermaid.append("    A --> T")
    mermaid.append("    T --> B")
    mermaid.append("    T -.bloqueia.-> F")
    mermaid.append("    T -.executado por.-> AG")

    # Styling
    mermaid.append("")
    mermaid.append("    style A fill:#e1f5ff,stroke:#0288d1")
    mermaid.append("    style T fill:#fff9c4,stroke:#fbc02d")
    mermaid.append("    style B fill:#c8e6c9,stroke:#388e3c")
    mermaid.append("    style F fill:#ffcdd2,stroke:#c62828")
    mermaid.append("    style AG fill:#e1bee7,stroke:#8e24aa")

    return "\n".join(mermaid)


def generate_pipeline_diagram() -> str:
    """
    Gera diagrama do Pipeline de 7 Passos do MAAS.

    Returns:
        Código Mermaid para o diagrama
    """
    mermaid = ["graph LR"]
    mermaid.append("    direction LR")

    steps = [
        ("1. EXTRAIR", "#90caf9"),
        ("2. ATOMIZAR", "#90caf9"),
        ("3. SEQUENCIAR", "#fff59d"),
        ("4. ALOCAR", "#fff59d"),
        ("5. IMPLEMENTAR", "#a5d6a7"),
        ("6. MEDIR Ke", "#a5d6a7"),
        ("7. ITERAR", "#ef9a9a"),
    ]

    nodes = []
    for i, (step, color) in enumerate(steps):
        node_id = f"S{i}"
        mermaid.append(f"    {node_id}[{step}]")
        nodes.append(node_id)

    # Connect sequentially
    for i in range(len(nodes) - 1):
        mermaid.append(f"    {nodes[i]} --> {nodes[i + 1]}")

    # Add iteration loop back
    mermaid.append(f"    {nodes[-1]} -.aprender.-> {nodes[0]}")

    # Styling
    mermaid.append("")
    for i, (_, color) in enumerate(steps):
        node_id = nodes[i]
        mermaid.append(f"    style {node_id} fill:{color},stroke:#424242")

    return "\n".join(mermaid)


def parse_markdown_atoms(markdown_content: str) -> List[Dict]:
    """
    Extrai átomos de um documento Markdown MAAS.

    Busca por tabelas ou listas que seguem o padrão MAAS:
    | ID | Nome | Input | Decisão | Output | Agente | Fricção |

    Args:
        markdown_content: Conteúdo Markdown

    Returns:
        Lista de átomos extraídos
    """
    atoms = []

    # Try to find atom table
    lines = markdown_content.split('\n')
    in_table = False
    header_found = False

    for i, line in enumerate(lines):
        # Look for table header with atom columns
        if 'ID' in line and 'Nome' in line and 'Input' in line and 'Output' in line:
            in_table = True
            header_found = True
            continue

        if in_table:
            # Skip separator line
            if line.startswith('|---'):
                continue

            # End of table
            if not line.startswith('|') or line.strip() == '|':
                break

            # Parse table row
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            if len(cells) >= 4:
                atoms.append({
                    "id": cells[0].replace('[', '').replace(']', ''),
                    "name": cells[1],
                    "input": cells[2] if len(cells) > 2 else "",
                    "decision": cells[3] if len(cells) > 3 else "",
                    "output": cells[4] if len(cells) > 4 else "",
                    "agent": cells[5] if len(cells) > 5 else "SISTEMA",
                    "friction": cells[6] if len(cells) > 6 else "",
                })

    return atoms


def generate_all_diagrams(markdown_content: str) -> Dict[str, str]:
    """
    Gera todos os diagramas para um documento MAAS.

    Args:
        markdown_content: Conteúdo Markdown do documento

    Returns:
        Dicionário com todos os diagramas gerados
    """
    atoms = parse_markdown_atoms(markdown_content)

    diagrams = {
        "four_causes": generate_four_causes(),
        "anatomy": generate_anatomy_diagram(),
        "pipeline": generate_pipeline_diagram(),
        "ke_equation": generate_ke_equation(),
    }

    if atoms:
        diagrams["dag"] = generate_dag(atoms)
        diagrams["agent_matrix"] = generate_agent_matrix(atoms)

    return diagrams


# ===========================================
# CLI INTERFACE
# ===========================================

def main():
    """Ponto de entrada para linha de comando."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Gera diagramas Mermaid para documentação MAAS'
    )
    parser.add_argument('input', help='Arquivo Markdown MAAS')
    parser.add_argument('-o', '--output', help='Arquivo de saída (JSON com diagramas)')
    parser.add_argument('-t', '--type', choices=['dag', 'atom', 'agents', 'ke', 'causes', 'anatomy', 'pipeline', 'all'],
                       default='all', help='Tipo de diagrama')

    args = parser.parse_args()

    # Read markdown
    with open(args.input, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generate diagrams
    diagrams = generate_all_diagrams(content)

    # Filter by type if specified
    if args.type != 'all':
        type_map = {
            'dag': 'dag',
            'agents': 'agent_matrix',
            'ke': 'ke_equation',
            'causes': 'four_causes',
            'anatomy': 'anatomy',
            'pipeline': 'pipeline',
        }
        if args.type in type_map:
            diagrams = {type_map[args.type]: diagrams[type_map[args.type]]}

    # Output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(diagrams, f, indent=2, ensure_ascii=False)
        print(f"✅ Diagramas salvos em: {args.output}")
    else:
        for name, diagram in diagrams.items():
            print(f"\n{'='*60}")
            print(f"Diagram: {name}")
            print('='*60)
            print('```mermaid')
            print(diagram)
            print('```')


if __name__ == '__main__':
    main()
