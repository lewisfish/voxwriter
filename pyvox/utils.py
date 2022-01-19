def chunks(listy, n):
    """Yield successive n-sized chunks from listy."""
    for i in range(0, len(listy), n):
        yield listy[i:i + n]
