"""CLI for the mini-unreachable fixture."""


def band():
    """Compute the phonon dispersion along a high-symmetry path."""
    return {"frequencies": []}


def main(argv=None):
    args = list(argv or [])
    if not args or args[0] != "band":
        print("usage: mini-unreachable band")
        return 2
    print(band())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
