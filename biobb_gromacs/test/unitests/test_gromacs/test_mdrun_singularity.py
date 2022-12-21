from biobb_common.tools import test_fixtures as fx
from biobb_gromacs.gromacs.mdrun import mdrun
from biobb_gromacs.gromacs.common import gmx_rms
import pytest


class TestMdrunSingularity():
    def setup_class(self):
        fx.test_setup(self, 'mdrun_singularity')

    def teardown_class(self):
        #pass
        fx.test_teardown(self)

    @pytest.mark.skip(reason="singularity currently not available")
    def test_mdrun_singularity(self):
        returncode = mdrun(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_trr_path'])
        assert gmx_rms(self.paths['output_trr_path'], self.paths['ref_output_trr_path'], self.paths['input_tpr_path'], self.properties.get('binary_path','gmx'))
        assert fx.not_empty(self.paths['output_gro_path'])
        assert fx.not_empty(self.paths['output_edr_path'])
        assert fx.not_empty(self.paths['output_log_path'])
        assert fx.exe_success(returncode)
