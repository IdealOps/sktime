# -*- coding: utf-8 -*-
# copyright: sktime developers, BSD-3-Clause License (see LICENSE file)
"""
Extension template for unsupervised sequence aligners.

Purpose of this implementation template:
    quick implementation of new estimators following the template
    NOT a concrete class to import! This is NOT a base class or concrete class!
    This is to be used as a "fill-in" coding template.

How to use this implementation template to implement a new estimator:
- make a copy of the template in a suitable location, give it a descriptive name.
- work through all the "todo" comments below
- fill in code for mandatory methods, and optionally for optional methods
- do not write to reserved variables: is_fitted, _is_fitted, _tags, _tags_dynamic, _X
- you can add more private methods, but do not override BaseEstimator's private methods
    an easy way to be safe is to prefix your methods with "_custom"
- change docstrings for functions and the file
- ensure interface compatibility by sktime.utils.estimator_checks.check_estimator
- once complete: use as a local library, or contribute to sktime via PR
- more details:
  https://www.sktime.net/en/stable/developer_guide/add_estimators.html

Mandatory implements:
    fitting                 - _fit(self, X, Z)
    get alignment           - _get_alignment(self)

Optional implements:
    data conversion and capabilities tags - _tags
    get overall distance (scalar)         - _get_distance(self)
    get alignment distance matrix         - _get_distance_matrix(self)

Testing - required for sktime test framework and check_estimator usage:
    get default parameters for test instance(s) - get_test_params()

copyright: sktime developers, BSD-3-Clause License (see LICENSE file)
"""

from sktime.alignment.base import BaseAligner

# todo: add any necessary imports here

# todo: if any imports are sktime soft dependencies:
# make sure to fill in the "python_dependencies" tag with the package import name


class MyAligner(BaseAligner):
    """Custom time series aligner. todo: write docstring.

    todo: describe your custom time series aligner here

    Hyper-parameters
    ----------------
    parama : int
        descriptive explanation of parama
    paramb : string, optional (default='default')
        descriptive explanation of paramb
    paramc : boolean, optional (default= whether paramb is not the default)
        descriptive explanation of paramc
    and so on

    Components
    ----------
    est : sktime.estimator, BaseEstimator descendant
        descriptive explanation of est
    est2: another estimator
        descriptive explanation of est2
    and so on
    """

    # optional todo: override base class estimator default tags here if necessary
    # these are the default values, only add if different to these.
    _tags = {
        "capability:multiple-alignment": False,  # can align more than two sequences?
        "capability:distance": False,  # does compute/return overall distance?
        "capability:distance-matrix": False,  # does compute/return distance matrix?
        "python_version": None,  # PEP 440 python version specifier to limit versions
    }

    # todo: add any hyper-parameters and components to constructor
    def __init__(self, est, parama, est2=None, paramb="default", paramc=None):
        # estimators should precede parameters
        #  if estimators have default values, set None and initalize below

        # todo: write any hyper-parameters and components to self
        self.est = est
        self.parama = parama
        self.paramb = paramb
        self.paramc = paramc

        # todo: change "MyAligner" to the name of the class
        super(MyAligner, self).__init__()

        # todo: optional, parameter checking logic (if applicable) should happen here
        # if writes derived values to self, should *not* overwrite self.parama etc
        # instead, write to self._parama, self._newparam (starting with _)

        # todo: default estimators should have None arg defaults
        #  and be initialized here
        #  do this only with default estimators, not with parameters
        # if est2 is None:
        #     self.estimator = MyDefaultEstimator()

        # todo: if tags of estimator depend on component tags, set these here
        #  only needed if estimator is a composite
        #  tags set in the constructor apply to the object and override the class
        #
        # example 1: conditional setting of a tag
        # if est.foo == 42:
        #   self.set_tags(handles-missing-data=True)
        # example 2: cloning tags from component
        #   self.clone_tags(est2, ["enforce_index_type", "handles-missing-data"])

    # todo: implement this, mandatory
    def _fit(self, X, Z=None):
        """Fit alignment given series/sequences to align.

            core logic

        Writes to self:
            Sets fitted model attributes ending in "_".

        Parameters
        ----------
        X : list of pd.DataFrame (Series) of length n
            collection of series to align
        Z : pd.DataFrame with n rows, optional
            metadata, i-th row of Z corresponds to i-th element of X
        """

        # implement here
        # IMPORTANT: avoid side effects to X, Z
        #
        # Note: if capability:multiple-alignment is False, then n=2 always
        #  i.e., X will always be of length 2, contain only two series
        #  if capability:multiple-alignment is True, _fit needs to deal with n>=2
        #
        # Note: when interfacing a model that has fit, with parameters
        #   that are not data (X, Z) or data-like,
        #   but model parameters, *don't* add as arguments to fit, but treat as follows:
        #   1. pass to constructor,  2. write to self in constructor,
        #   3. read from self in _fit,  4. pass to interfaced_model.fit in _fit

    # todo: implement this, mandatory
    def _get_alignment(self):
        """Return alignment for sequences/series passed in fit (iloc indices).

            core logic

        Behaviour: returns an alignment for sequences in X passed to fit
            model should be in fitted state, fitted model parameters read from self

        Accesses in self:
            Fitted model attributes ending in "_".

        Returns
        -------
        pd.DataFrame in alignment format, with columns 'ind'+str(i) for integer i
            cols contain iloc index of X[i] mapped to alignment coordinate for alignment
        """

        # implement here

    # todo: consider implementing this, optional
    # if implemented, set capability:distance tag to True
    def _get_distance(self):
        """Return overall distance of alignment.

            core logic

        Behaviour: returns overall distance corresponding to alignment
            not all aligners will return or implement this (optional)
        Accesses in self:
            Fitted model attributes ending in "_".

        Returns
        -------
        distance: float - overall distance between all elements of X passed to fit
        """

        # implement here

    # todo: consider implementing this, optional
    # if implemented, set capability:distance-matrix tag to True
    def _get_distance_matrix(self):
        """Return distance matrix of alignment.

            core logic

        Behaviour: returns pairwise distance matrix of alignment distances
            not all aligners will return or implement this (optional)

        Accesses in self:
            Fitted model attributes ending in "_".

        Returns
        -------
        distmat: an (n x n) np.array of floats, where n is length of X passed to fit
            [i,j]-th entry is alignment distance between X[i] and X[j] passed to fit
        """

        # implement here

    # todo: implement this if this is an estimator contributed to sktime
    #   or to run local automated unit and integration testing of estimator
    #   method should return default parameters, so that a test instance can be created
    @classmethod
    def get_test_params(cls, parameter_set="default"):
        """Return testing parameter settings for the estimator.

        Parameters
        ----------
        parameter_set : str, default="default"
            Name of the set of test parameters to return, for use in tests. If no
            special parameters are defined for a value, will return `"default"` set.
            There are currently no reserved values for aligners.

        Returns
        -------
        params : dict or list of dict, default = {}
            Parameters to create testing instances of the class
            Each dict are parameters to construct an "interesting" test instance, i.e.,
            `MyClass(**params)` or `MyClass(**params[i])` creates a valid test instance.
            `create_test_instance` uses the first (or only) dictionary in `params`
        """

        # todo: set the testing parameters for the estimators
        # Testing parameters can be dictionary or list of dictionaries.
        # Testing parameter choice should cover internal cases well.
        #   for "simple" extension, ignore the parameter_set argument.
        #
        # this method can, if required, use:
        #   class properties (e.g., inherited); parent class test case
        #   imported objects such as estimators from sktime or sklearn
        # important: all such imports should be *inside get_test_params*, not at the top
        #            since imports are used only at testing time
        #
        # A good parameter set should primarily satisfy two criteria,
        #   1. Chosen set of parameters should have a low testing time,
        #      ideally in the magnitude of few seconds for the entire test suite.
        #       This is vital for the cases where default values result in
        #       "big" models which not only increases test time but also
        #       run into the risk of test workers crashing.
        #   2. There should be a minimum two such parameter sets with different
        #      sets of values to ensure a wide range of code coverage is provided.
        #
        # example 1: specify params as dictionary
        # any number of params can be specified
        # params = {"est": value0, "parama": value1, "paramb": value2}
        #
        # example 2: specify params as list of dictionary
        # note: Only first dictionary will be used by create_test_instance
        # params = [{"est": value1, "parama": value2},
        #           {"est": value3, "parama": value4}]
        #
        # return params
