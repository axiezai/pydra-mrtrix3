import attr
import typing as ty 
from pydra import ShellCommandTask
from pydra.engine.specs import File, SpecInfo, ShellSpec, ShellOutSpec
from .base import MRTrix3BaseSpec
    

MRConvertInputSpec = SpecInfo(
    name="MRConvertInputs",
    fields=[
        (
            "in_file",
            attr.ib(
                type=File,
                metadata={
                    "position": 4,
                    "help_string": "input image",
                    "mandatory": True
                },
            ),
        ),
        (
            "out_file",
            attr.ib(
                type=str,
                metadata={
                    "position": 5,
                    "help_string": "output image",
                },
            ),
        ),
        (
            "coord",
            attr.ib(
                type=ty.List[float],
                metadata={
                    "argstr": "-coord",
                    "help_string": "extract data at the specific coordinatest",
                },
            ),
        ),
        (
            "vox",
            attr.ib(
                type=ty.List[float],
                metadata={
                    "argstr": "-vox",
                    "help_string": "change the voxel dimensions",
                },
            ),
        ),
        (
            "axes",
            attr.ib(
                type=ty.List[int],
                metadata={
                    "argstr": "-axes",
                    "help_string": "specify the axes that will be used",
                },
            ),
        ),
        (
            "scaling",
            attr.ib(
                type=ty.List[float],
                metadata={
                    "argstr": "-scaling",
                    "help_string": "specify the data scaling parameter",
                },
            ),
        ),
        (
            "export_grad",
            attr.ib(
                type=str,
                metadata={
                    "argstr": "-export_grad_mrtrix",
                    "position": 3,
                    "help_string":  "export new gradient files in mrtrix3 format"
                },
            ),
        ),
        (
            "export_json",
            attr.ib(
                type=str,
                metadata={
                    "argstr": "-json_export",
                    "help_string": "export image headet to JSON file"
                },
            ),
        ),
    ],
    bases=(MRTrix3BaseSpec,),
)

MRConvertOutputSpec = SpecInfo(
    name = "MRConvertOutputs",
    fields=[
        (
            "out_file",
            attr.ib(
                type=File,
                metadata={
                    "help_string": "output image",
                    "output_file_template": "dwi.mif"
                },
            ),
        ),
        (
            "out_bfile",
            attr.ib(
                type=File,
                metadata={
                    "help_string": "output .b gradient file in mrtrix3 format",
                    "output_file_template": "dwi.b"
                },
            ),
        ),
        (
            "out_json",
            attr.ib(
                type=File,
                metadata={
                    "help_string": "output JSON file of image header",
                    "output_file_template": "dwi.json"
                },
            ),
        ),
    ],
    bases=(ShellOutSpec,),
)


#  Create task for pydra
MRConvert =  ShellCommandTask(
    name='MRConvert',
    executable="mrconvert",
    in_file="/Users/xxie/sample_data/tinnitus2/sub-MINN294/ses-01/dwi/sub-MINN294_ses-01_run-1_dwi.nii",
    grad_fsl=(
        "/Users/xxie/sample_data/tinnitus2/sub-MINN294/ses-01/dwi/sub-MINN294_ses-01_run-1_dwi.bvec",
        "/Users/xxie/sample_data/tinnitus2/sub-MINN294/ses-01/dwi/sub-MINN294_ses-01_run-1_dwi.bval"
        ),
    export_grad="sub-MINN294_ses-01_run-1.b",
    out_file="sub-MINN294_ses-01_run-1.mif",
    input_spec=MRConvertInputSpec,
    output_spec=MRConvertOutputSpec
)

# try running the task:
print(MRConvert.cmdline)
print(MRConvert.inputs.executable)
assert MRConvert.inputs.executable == "mrconvert"
MRConvert()
MRConvert.result()