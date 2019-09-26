from starfish import Experiment


def MERFISH(use_test_data: bool = False) -> Experiment:
    """
    Loads an experiment with a single field of view of MERFISH data derived from cultured U2-OS
    cells, published in the following manuscript:

    `<https://doi.org/10.1073/pnas.1612826113>`_

    The data consist of 16 images from 8 rounds, 2 channels, and a single z-plane. Each image is
    (2048, 2048) (y, x)

    Parameters
    ----------
    use_test_data: bool
        If True, returns a cropped Experiment where tiles are (205, 405) (y, x)

    Returns
    -------
    Experiment
    """
    if use_test_data:
        return Experiment.from_json(
            "https://d2nhj9g34unfro.cloudfront.net/20181005/MERFISH-TEST/experiment.json")
    return Experiment.from_json("https://d2nhj9g34unfro.cloudfront.net/browse/formatted/"
                                "MERFISH/20190511/experiment.json")


def allen_smFISH(use_test_data: bool = False) -> Experiment:
    """
    Loads an experiment with a single round from a single field of view of sequential smFISH data
    taken from mouse primary visual cortex. These data are unpublished, and were kindly
    contributed by the Allen Institute for Brain Science as a part of the SpaceTx consortium
    project.

    The data consist of 102 images from 1 round, 3 channels, and 33 z-planes. Each image is
    (2048, 2048) (y, x). There are no test data.

    Parameters
    ----------
    use_test_data : bool
        Not used.

    Returns
    -------
    Experiment
    """
    if use_test_data:
        return Experiment.from_json(
            "https://d2nhj9g34unfro.cloudfront.net/20181005/allen_smFISH/experiment.json")
    return Experiment.from_json(
        "https://d26bikfyahveg8.cloudfront.net/smFISH/mouse/formatted_with_DAPI/experiment.json")


def DARTFISH(use_test_data: bool = False) -> Experiment:
    """
    Loads an experiment with a single field of view from unpublished data generated with DARTFISH v1
    2017, produced by imaging human occipital cortex. These data were donated by the Zhang lab as
    part of the SpaceTx consortium project.

    The data consist of 18 images from 3 channels, 6 rounds, and 1 z-plane. Each image is (998, 998)
    in (y, x).

    Parameters
    ----------
    use_test_data : bool
        If True, returns a cropped Experiment where tiles are (170, 290) in (y, x)

    Returns
    -------
    Experiment
    """
    if use_test_data:
        return Experiment.from_json(
            "https://d2nhj9g34unfro.cloudfront.net/20181005/DARTFISH-TEST/experiment.json")
    return Experiment.from_json(
        "https://d2nhj9g34unfro.cloudfront.net/20181005/DARTFISH/experiment.json")


def ISS(use_test_data: bool = False) -> Experiment:
    """
    Loads an experiment containing a single field of view of In-Situ Sequencing data created by
    imaging human breast cancer tissue. The complete dataset is published:

    `<https://doi.org/10.1038/nmeth.2563>`_

    The data consist of 16 images from 4 channels, 4 rounds, and a single z-plane. Each image is
    (1044, 1390) in (y, x)

    Parameters
    ----------
    use_test_data : bool
        If True, returns a cropped Experiment where images are (140, 200) in (y, x)

    Returns
    -------
    Experiment
    """
    if use_test_data:
        return Experiment.from_json(
            "https://d2nhj9g34unfro.cloudfront.net/20181005/ISS-TEST/experiment.json")
    return Experiment.from_json(
        "https://d2nhj9g34unfro.cloudfront.net/browse/formatted/iss/20190506/experiment.json")


def osmFISH(use_test_data: bool = False) -> Experiment:
    """
    Loads an experiment containing 3 fields of view of osmFISH data generated by imaging mouse
    sematosensory cortex. The complete dataset is published:

    `<https://doi.org/10.1038/s41592-018-0175-z>`_

    The data consist of 1755 images per field of view, taken over 13 rounds, 3 channels, and 45
    z-planes. Each image is (2048, 2048) in (y, x)

    Parameters
    ----------
    use_test_data : bool
        If True, return a single round from one field of view, suitable for testing. The images are
        still (2048, 2048) in (y, x)

    Returns
    -------
    Experiment
    """
    if use_test_data:
        return Experiment.from_json(
            "https://d2nhj9g34unfro.cloudfront.net/browse/formatted/20181217/osmFISH/"
            "experiment.json"
        )
    return Experiment.from_json(
        "https://d26bikfyahveg8.cloudfront.net/osmFISH/formatted/20190626/experiment.json")


def BaristaSeq(use_test_data: bool = False) -> Experiment:
    """Loads a BaristaSeq dataset generated from mouse visual cortex. The extracted field of view
    comes from an internal layer of V1 (range: 2-5). These data are published here:

    `<https://doi.org/10.1093/nar/gkx1206>`_

    The data consist of 204 images acquired from 3 rounds, 4 channels, and 17 z-planes. Each image
    is (1000, 800) in (y, x)

    Parameters
    ----------
    use_test_data : bool
        Not used.

    Returns
    -------
    Experiment
    """
    return Experiment.from_json(
        "https://d2nhj9g34unfro.cloudfront.net/browse/formatted/20181028/"
        "BaristaSeq/cropped_formatted/experiment.json"
    )


def ImagingMassCytometry(use_test_data: bool = False) -> Experiment:
    """
    Loads an Imaging Mass Cytometry dataset donated to starfish by Denis Shapiro. This dataset
    consists of 52 fields of view.

    Each field of view consists of 19 images acquired from 19 channels, 1 round, and 1 z-plane.
    Individual images have variable sizes, ranging from 400-500 pixels for each of (y, x).

    Parameters
    ----------
    use_test_data:
        Not used.

    Returns
    -------
    Experiment
    """
    return Experiment.from_json(
        "https://d2nhj9g34unfro.cloudfront.net/browse/formatted/20181023/"
        "imaging_cytof/BodenmillerBreastCancerSamples/experiment.json"
    )


def SeqFISH(use_test_data: bool = False) -> Experiment:
    """
    Loads a single field of view from a SeqFISH dataset generated from cultured mES cells. These
    data are published:

    `<https://doi.org/10.1016/j.cell.2018.05.035>`_

    This dataset contains 1140 images acquired across 12 channels, 4 imaging rounds, and 29
    z-planes. Each image is (2048, 2048) in (y, x)

    Parameters
    ----------
    use_test_data : bool
        If true, return a cropped Experiment where images are (280, 280) in (y, x)

    Returns
    -------
    Experiment
    """
    suffix = "-TEST" if use_test_data else ""
    url = (
        f"https://d2nhj9g34unfro.cloudfront.net/browse/formatted/20181211/"
        f"seqfish{suffix}/experiment.json"
    )
    return Experiment.from_json(url)


def STARmap(use_test_data: bool = False) -> Experiment:
    """
    Loads a STARmap field of view generated from mouse primary visual cortex. These data are
    published:

    `<https://doi.org/10.1126/science.aat5691>`_

    This dataset contains 696 images acquired across 6 rounds, 4 channels, and 29 z-planes. Each
    image is (1024, 1024) in (y, x)

    Parameters
    ----------
    use_test_data : bool
        Not used.

    Returns
    -------
    Experiment
    """
    url = (
        "https://d2nhj9g34unfro.cloudfront.net/browse/formatted/20190309/"
        "starmap/experiment.json"
    )
    return Experiment.from_json(url)
