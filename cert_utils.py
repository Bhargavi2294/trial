def required_certifications(pcb_name):
    """
    Determines required certifications based on PCB name keywords.
    """
    name_lower = pcb_name.lower()
    required = []

    # Common certs by PCB use-case
    if 'consumer' in name_lower or 'electronics' in name_lower:
        required += ['CE', 'RoHS', 'UL']
    if 'industrial' in name_lower or 'power' in name_lower:
        required += ['CE', 'RoHS', 'UL', 'ISO 9001']
    if 'medical' in name_lower:
        required += ['CE (Medical)', 'ISO 13485', 'FDA', 'RoHS']
    if 'automotive' in name_lower:
        required += ['ISO / TS 16949', 'CE', 'RoHS']

    # If nothing matched, suggest general
    if not required:
        required = ['CE', 'RoHS']

    # Deduplicate
    return sorted(set(required))
