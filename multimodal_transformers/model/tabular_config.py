import json

class TabularConfig:
    r""" Config used for tabular combiner



    Args:
        mlp_division (int): how much to decrease each MLP dim for each additional layer
        combine_feat_method (str): The method to combine categorical and numerical features.
            See :obj:`TabularFeatCombiner` for details on the supported methods.
        mlp_dropout (float): dropout ratio used for MLP layers
        numerical_bn (bool): whether to use batchnorm on numerical features
        use_simple_classifier (bool): whether to use single layer or MLP as final classifier
        mlp_act (str): the activation function to use for finetuning layers
        gating_beta (float): the beta hyperparameters used for gating tabular data
            see the paper `Integrating Multimodal Information in Large Pretrained Transformers <https://www.aclweb.org/anthology/2020.acl-main.214.pdf>`_ for details
        numerical_feat_dim (int): the number of numerical features
        cat_feat_dim (int): the number of categorical features

    """
    def __init__(self,
                 num_labels,
                 mlp_division=4,
                 combine_feat_method='text_only',
                 mlp_dropout=0.1,
                 numerical_bn=True,
                 use_simple_classifier=True,
                 mlp_act='relu',
                 gating_beta=0.2,
                 numerical_feat_dim=0,
                 cat_feat_dim=0,
                 cat_feat_names="Auto",
                 **kwargs
                 ):
        self.mlp_division = mlp_division
        self.combine_feat_method = combine_feat_method
        self.mlp_dropout = mlp_dropout
        self.numerical_bn = numerical_bn
        self.use_simple_classifier = use_simple_classifier
        self.mlp_act = mlp_act
        self.gating_beta = gating_beta
        self.numerical_feat_dim = numerical_feat_dim
        self.cat_feat_dim = cat_feat_dim
        self.cat_feat_names = "Auto"
        self.num_labels = num_labels

    def to_dict(self):
        """
        Serializes this instance while replace `Enum` by their values (for JSON serialization support).
        """
        return {'mlp_division': self.mlp_division, 'combine_feat_method': self.combine_feat_method, 'mlp_dropout': self.mlp_dropout, 'numerical_bn':self.numerical_bn,
                'use_simple_classifier': self.use_simple_classifier, 'mlp_act': self.mlp_act, 'gating_beta': self.gating_beta, 'numerical_feat_dim':self.numerical_feat_dim,
                'cat_feat_dim': self.cat_feat_dim, 'num_labels': self.num_labels}

    def __repr__(self):
        return(self.to_json_string())


    def to_json_string(self):
        """
        Serializes this instance to a JSON string.
        """
        return json.dumps(self.to_dict(), indent=2)
