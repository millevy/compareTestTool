import ipdb
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from pylero.test_run import TestRun
from pylero.work_item import TestCase

def main():
    project_id_RHELOpenStackPlatform = "RHELOpenStackPlatform"
    project_id_RHOSO = "RHOSO"
    tr = TestRun("20230829-1659", project_id = project_id)
    results_dict = {}
    for test in tr.records:
        test_id = test.test_case_id
        tc = TestCase(project_id=project_id, work_item_id=test_id)
        project_dict[test_id]: {
            project_id_RHELOpenStackPlatform: {
                "Test_name": tc.title,
                "Test_path": tc.automation_script
            },
            project_id_RHOSO: {
                "Test_name": tc.title,
                "Test_path": tc.automation_script
        }


    ipdb.set_trace()

if __name__ == "__main__":
    main()

