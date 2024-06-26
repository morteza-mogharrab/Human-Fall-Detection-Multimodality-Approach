import os
import data_formatters.mobiact
import data_formatters.notch
import data_formatters.smartfall
import data_formatters.dlr


class ExperimentConfig(object):
  """Defines experiment configs and paths to outputs.

  Attributes:
    root_folder: Root folder to contain all experimental outputs.
    data_folder: Folder to store data for experiment.
    model_folder: Folder to store serialised models.
    results_folder: Folder to store results.
    data_csv_path: Path to primary data csv file used in experiment.
    hyperparam_iterations: Default number of random search iterations for
      experiment.
  """

  default_experiments = ['mobiact', 'dlr', 'notch', 'smartfall']

  def __init__(self, experiment='volatility', root_folder=None):
    """Creates configs based on default experiment chosen.

    Args:
      experiment: Name of experiment.
      root_folder: Root folder to save all outputs of training.
    """

    if experiment not in self.default_experiments:
      raise ValueError('Unrecognised experiment={}'.format(experiment))

    # Defines all relevant paths
    if root_folder is None:
      root_folder = os.path.join(
          os.path.dirname(os.path.realpath(__file__)), '..', 'outputs')
      print('Using root folder {}'.format(root_folder))

    self.root_folder = root_folder
    self.experiment = experiment
    self.data_folder = 'dataset/'
    self.model_folder = os.path.join(root_folder, 'saved_models', experiment)
    self.results_folder = os.path.join(root_folder, 'results', experiment)

    # Creates folders if they don't exist
    for relevant_directory in [
        self.root_folder, self.data_folder, self.model_folder,
        self.results_folder
    ]:
      if not os.path.exists(relevant_directory):
        os.makedirs(relevant_directory)

  @property
  def data_csv_path(self):
    csv_path = {
        'mobiact': 'mobiact_preprocessed/',
        'notch': 'notch_dataset/',
        'smartfall': 'smartFall_dataset/',
        'dlr': 'dlr_preprocessed/'
    }

    return os.path.join(self.data_folder, csv_path[self.experiment])

  @property
  def hyperparam_iterations(self):

    return 240 if self.experiment == 'volatility' else 60

  def make_data_formatter(self):
    """Gets a data formatter object for experiment.

    Returns:
      Default DataFormatter per experiment.
    """

    data_formatter_class = {
        'mobiact': data_formatters.mobiact.MobiActFormatter,
        'notch': data_formatters.notch.NotchFormatter,
        'smartfall': data_formatters.smartfall.SmartFallFormatter,
        'dlr': data_formatters.dlr.DLRFormatter
    }

    return data_formatter_class[self.experiment]()
