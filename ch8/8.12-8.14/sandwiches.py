def sandwich_builder(*items):
    """Build a sandwich from the list of items provided"""
    print(f"\nYour sandwich will have the following items:")
    for item in items:
        print(f"- {item}")


sandwich_builder('lettuce', 'tomato', 'onion', 'pickles', 'mayo')

sandwich_builder('onions', 'pickles', 'mayo')

sandwich_builder('lettuce', 'tomato', 'onion', 'pickles', 'mayo',
                 'onions', 'pickles', 'mayo')

