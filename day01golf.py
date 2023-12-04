print(
    sum(
        int(
            filter(lambda x: x.isnumeric(), line).__next__()
            + filter(lambda x: x.isnumeric(), reversed(line)).__next__()
        )
        for line in open(0, "r").readlines()
    )
)
