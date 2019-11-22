import os
import sys

import numpy as np
import pandas as pd

import starfish
from starfish.types import Features

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(starfish.__file__)))
os.environ["USE_TEST_DATA"] = "1"
sys.path.append(os.path.join(ROOT_DIR, "notebooks", "py"))


def test_merfish_pipeline_cropped_data():

    # set random seed to errors provoked by optimization functions
    np.random.seed(777)

    merfish = __import__('MERFISH')

    primary_image = merfish.imgs

    expected_primary_image = np.array(
        [[0.09593347, 0.09794766, 0.10089265, 0.10231174, 0.10133516,
          0.10002289, 0.1035172, 0.10647745, 0.10809491, 0.10769818],
         [0.09840543, 0.09710842, 0.09787137, 0.10025177, 0.10017548,
          0.10102998, 0.10756085, 0.10952926, 0.10888838, 0.10472267],
         [0.09965667, 0.09999237, 0.10307469, 0.10264744, 0.10170138,
          0.10417334, 0.10580606, 0.10658427, 0.10473793, 0.10211337],
         [0.10383764, 0.10521096, 0.10623331, 0.10525673, 0.10400549,
          0.10115206, 0.10203708, 0.10415808, 0.10347143, 0.10434119],
         [0.10539406, 0.10548562, 0.10464637, 0.10547036, 0.10615702,
          0.10554665, 0.10327306, 0.09990082, 0.09980926, 0.10301366],
         [0.1085069, 0.10649271, 0.10342565, 0.10406653, 0.10771344,
          0.10740826, 0.10659953, 0.10327306, 0.10269322, 0.10246433],
         [0.11427481, 0.11221485, 0.10957504, 0.10734722, 0.10701152,
          0.10782025, 0.10749981, 0.10347143, 0.10150301, 0.10322728],
         [0.11642634, 0.11441215, 0.11172656, 0.1098497, 0.11038376,
          0.1097734, 0.1085832, 0.10276951, 0.10251011, 0.1017319],
         [0.11627375, 0.11638056, 0.11581598, 0.11468681, 0.11187915,
          0.11042954, 0.10994125, 0.10493629, 0.10205234, 0.10099947],
         [0.11708248, 0.11792172, 0.1163653, 0.11743343, 0.11384756,
          0.11157397, 0.10919356, 0.10666056, 0.10330358, 0.1016556]],
        dtype=np.float32
    )
    assert np.allclose(
        expected_primary_image,
        primary_image.xarray[5, 0, 0, 40:50, 45:55]
    )

    high_passed = merfish.high_passed

    expected_high_passed = np.array(
        [[0.00000000e+00, 0.00000000e+00, 1.09633317e-03, 1.99840278e-03,
          5.83776810e-04, 0.00000000e+00, 2.04111132e-03, 4.65832430e-03,
          5.91536953e-03, 5.13293567e-03],
         [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
          0.00000000e+00, 0.00000000e+00, 5.06116677e-03, 6.75149438e-03,
          5.81014126e-03, 1.30867042e-03],
         [0.00000000e+00, 0.00000000e+00, 4.04353003e-04, 0.00000000e+00,
          0.00000000e+00, 9.50735832e-04, 2.44306756e-03, 3.06733356e-03,
          1.02676533e-03, 0.00000000e+00],
         [0.00000000e+00, 9.25681404e-04, 1.93746323e-03, 9.78471914e-04,
          0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 6.93379398e-05,
          0.00000000e+00, 6.96662127e-05],
         [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
          7.19601658e-04, 4.23542969e-04, 0.00000000e+00, 0.00000000e+00,
          0.00000000e+00, 0.00000000e+00],
         [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
          1.03922332e-03, 1.31504616e-03, 1.06819853e-03, 0.00000000e+00,
          0.00000000e+00, 0.00000000e+00],
         [3.29251956e-03, 1.94998653e-03, 6.55281453e-05, 0.00000000e+00,
          0.00000000e+00, 7.41835209e-04, 1.23043721e-03, 0.00000000e+00,
          0.00000000e+00, 0.00000000e+00],
         [3.54986487e-03, 2.41864172e-03, 6.62828987e-04, 0.00000000e+00,
          1.30568280e-03, 1.73368034e-03, 1.55901266e-03, 0.00000000e+00,
          0.00000000e+00, 0.00000000e+00],
         [1.86399753e-03, 2.96097458e-03, 3.44559705e-03, 3.42158093e-03,
          1.77239523e-03, 1.51152371e-03, 2.18335022e-03, 0.00000000e+00,
          0.00000000e+00, 0.00000000e+00],
         [1.52147513e-03, 3.41107862e-03, 2.98134040e-03, 5.24483122e-03,
          2.91270155e-03, 1.91782816e-03, 7.70164461e-04, 0.00000000e+00,
          0.00000000e+00, 0.00000000e+00]],
        dtype=np.float32
    )

    assert np.allclose(
        expected_high_passed,
        high_passed.xarray[5, 0, 0, 40:50, 45:55]
    )

    deconvolved = merfish.deconvolved

    # assert that the deconvolved data is correct
    expected_deconvolved_values = np.array(
        [[5.09203559e-08, 3.99730743e-06, 6.02244254e-05, 2.32111895e-04,
          4.38709190e-04, 8.47828167e-04, 2.31795525e-03, 4.93136980e-03,
          6.48643868e-03, 5.54422149e-03],
         [6.60923627e-09, 8.63586365e-07, 2.01752755e-05, 1.16822011e-04,
          3.61390965e-04, 1.12474535e-03, 3.94705823e-03, 7.74383964e-03,
          7.71820499e-03, 4.32695169e-03],
         [2.75848997e-08, 1.61227229e-06, 2.54613860e-05, 1.19236727e-04,
          3.09234048e-04, 7.16167502e-04, 1.58700964e-03, 1.76539237e-03,
          1.09438866e-03, 4.09075874e-04],
         [3.65397710e-07, 5.31683509e-06, 3.80132406e-05, 1.12353613e-04,
          1.95116038e-04, 2.41404981e-04, 2.24630377e-04, 9.43155683e-05,
          2.73999813e-05, 6.17785554e-06],
         [5.46700721e-06, 1.80027182e-05, 5.35344516e-05, 9.94052753e-05,
          1.26581814e-04, 9.04178087e-05, 3.57624158e-05, 5.10032260e-06,
          5.79008656e-07, 7.04589382e-08],
         [8.61567096e-05, 7.29738385e-05, 8.63802634e-05, 9.99508338e-05,
          1.03577157e-04, 5.16096479e-05, 1.08268950e-05, 6.05715229e-07,
          2.42539251e-08, 1.29870636e-09],
         [7.39652023e-04, 3.09492985e-04, 2.13101332e-04, 1.80898453e-04,
          1.64827768e-04, 6.73260292e-05, 9.81487574e-06, 3.08488524e-07,
          5.28791411e-09, 1.09961575e-10],
         [2.57341471e-03, 1.17084652e-03, 8.95523408e-04, 7.92693347e-04,
          6.90109446e-04, 2.41029964e-04, 2.48702818e-05, 4.80789140e-07,
          3.64816422e-09, 2.91480694e-11],
         [1.90123543e-03, 1.50269351e-03, 2.15703435e-03, 3.06695886e-03,
          3.33567802e-03, 1.16718537e-03, 8.78327410e-05, 1.01623175e-06,
          3.37340489e-09, 1.54701668e-11],
         [4.64172917e-04, 9.28683614e-04, 3.45791667e-03, 9.42163169e-03,
          1.35401925e-02, 4.78239777e-03, 2.67850235e-04, 1.93931282e-06,
          3.70911546e-09, 2.12953006e-11]],
        dtype=np.float32
    )

    assert np.allclose(
        expected_deconvolved_values,
        deconvolved.xarray[5, 0, 0, 40:50, 45:55]
    )

    low_passed = merfish.low_passed

    expected_low_passed = np.array(
        [[4.45761580e-05, 1.44771271e-04, 3.09169467e-04, 4.67986334e-04,
          6.62159640e-04, 1.19392306e-03, 2.28226627e-03, 3.48766940e-03,
          3.97101697e-03, 3.62804998e-03],
         [7.00449118e-06, 3.26076297e-05, 1.02158629e-04, 2.46965181e-04,
          5.71789744e-04, 1.34325807e-03, 2.67716567e-03, 3.93851241e-03,
          4.17785347e-03, 3.45580117e-03],
         [4.04047387e-06, 1.80518000e-05, 6.36266996e-05, 1.73476015e-04,
          4.19444550e-04, 9.40128346e-04, 1.72989990e-03, 2.34171189e-03,
          2.28049955e-03, 1.71259057e-03],
         [1.57209906e-05, 2.53937105e-05, 6.02017462e-05, 1.28976928e-04,
          2.42699709e-04, 4.23678226e-04, 6.40416751e-04, 7.47716404e-04,
          6.46630186e-04, 4.36260569e-04],
         [1.05800158e-04, 7.10653621e-05, 7.99275367e-05, 1.10497269e-04,
          1.40035016e-04, 1.56843817e-04, 1.59643838e-04, 1.40404547e-04,
          1.00042482e-04, 5.85194066e-05],
         [5.13978768e-04, 2.62178277e-04, 1.82077172e-04, 1.66789090e-04,
          1.46720806e-04, 1.00256046e-04, 5.19661735e-05, 2.29582001e-05,
          9.93347021e-06, 4.38366806e-06],
         [1.45876023e-03, 7.50999665e-04, 5.23792463e-04, 4.76917106e-04,
          3.98246251e-04, 2.32851235e-04, 8.44381721e-05, 1.83961110e-05,
          2.55606847e-06, 3.19765519e-07],
         [2.30599311e-03, 1.39650132e-03, 1.29861617e-03, 1.49804540e-03,
          1.40797370e-03, 8.51143152e-04, 2.99671636e-04, 5.86564893e-05,
          6.23098504e-06, 3.58599010e-07],
         [2.05918634e-03, 1.74055109e-03, 2.48767645e-03, 3.70587152e-03,
          3.92567413e-03, 2.49905908e-03, 8.93056858e-04, 1.72159620e-04,
          1.74454071e-05, 9.34996422e-07],
         [1.12141343e-03, 1.55859930e-03, 3.33423750e-03, 6.02289755e-03,
          7.02448748e-03, 4.70918510e-03, 1.73011539e-03, 3.36037599e-04,
          3.36604389e-05, 2.04959770e-06]],
        dtype=np.float32
    )
    assert np.allclose(
        expected_low_passed,
        low_passed.xarray[5, 0, 0, 40:50, 45:55]
    )

    scaled_image = merfish.filtered_imgs

    # assert that the scaled data is correct
    expected_scaled_low_passed = np.array(
        [[5.60925116e-07, 1.82173255e-06, 3.89044089e-06, 5.88891680e-06,
          8.33230115e-06, 1.50237584e-05, 2.87189505e-05, 4.38871684e-05,
          4.99693815e-05, 4.56536509e-05],
         [8.81411779e-08, 4.10318847e-07, 1.28551540e-06, 3.10769201e-06,
          7.19512946e-06, 1.69029190e-05, 3.36881749e-05, 4.95603599e-05,
          5.25721152e-05, 4.34861540e-05],
         [5.08433935e-08, 2.27155240e-07, 8.00648024e-07, 2.18293940e-06,
          5.27809016e-06, 1.18301268e-05, 2.17682355e-05, 2.94669844e-05,
          2.86967188e-05, 2.15504224e-05],
         [1.97825443e-07, 3.19542323e-07, 7.57550026e-07, 1.62298409e-06,
          3.05401727e-06, 5.33136472e-06, 8.05869877e-06, 9.40890641e-06,
          8.13688530e-06, 5.48969501e-06],
         [1.33133869e-06, 8.94252594e-07, 1.00576995e-06, 1.39044494e-06,
          1.76213382e-06, 1.97364784e-06, 2.00888189e-06, 1.76678384e-06,
          1.25888687e-06, 7.36380287e-07],
         [6.46766375e-06, 3.29912632e-06, 2.29117222e-06, 2.09879431e-06,
          1.84626458e-06, 1.26157420e-06, 6.53917539e-07, 2.88895023e-07,
          1.24998053e-07, 5.51619870e-08],
         [1.83563425e-05, 9.45022111e-06, 6.59115449e-06, 6.00129715e-06,
          5.01134082e-06, 2.93008884e-06, 1.06252969e-06, 2.31487888e-07,
          3.21643476e-08, 4.02377687e-09],
         [2.90175176e-05, 1.75729056e-05, 1.63411660e-05, 1.88506892e-05,
          1.77172697e-05, 1.07103797e-05, 3.77092488e-06, 7.38105257e-07,
          7.84077443e-08, 4.51243887e-09],
         [2.59118187e-05, 2.19022641e-05, 3.13037344e-05, 4.66329184e-05,
          4.93988118e-05, 3.14469653e-05, 1.12378011e-05, 2.16637454e-06,
          2.19524679e-07, 1.17655485e-08],
         [1.41113314e-05, 1.96126693e-05, 4.19564531e-05, 7.57892703e-05,
          8.83928005e-05, 5.92581382e-05, 2.17709458e-05, 4.22853691e-06,
          4.23566917e-07, 2.57911594e-08]],
        dtype=np.float32
    )
    assert np.allclose(
        expected_scaled_low_passed,
        scaled_image.xarray[5, 0, 0, 40:50, 45:55]
    )

    spot_intensities = merfish.initial_spot_intensities

    # verify that the number of spots are correct
    spots_passing_filters = spot_intensities[Features.PASSES_THRESHOLDS].sum()
    assert spots_passing_filters == 1410

    # compare to paper results
    bench = pd.read_csv('https://d2nhj9g34unfro.cloudfront.net/MERFISH/benchmark_results.csv',
                        dtype={'barcode': object})
    benchmark_counts = bench.groupby('gene')['gene'].count()

    spot_intensities_passing_filters = spot_intensities.where(
        spot_intensities[Features.PASSES_THRESHOLDS], drop=True
    )
    genes, counts = np.unique(spot_intensities_passing_filters[Features.TARGET], return_counts=True)
    result_counts = pd.Series(counts, index=genes).sort_values(ascending=False)[:5]

    # assert that number of high-expression detected genes are correct
    expected_counts = pd.Series(
        [107, 59, 46, 32, 32],
        index=('MALAT1', 'SRRM2', 'FASN', 'IGF2R', 'TLN1')
    )
    assert np.array_equal(
        expected_counts.values,
        result_counts.values
    )
    assert np.array_equal(
        expected_counts.index,
        result_counts.index
    )

    tmp = pd.concat([result_counts, benchmark_counts], join='inner', axis=1).values

    corrcoef = np.corrcoef(tmp[:, 1], tmp[:, 0])[0, 1]

    assert np.round(corrcoef, 4) == 0.8427
