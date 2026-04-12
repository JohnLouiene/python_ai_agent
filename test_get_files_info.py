from functions.get_files_info import get_files_info

def test(working_dir, directory="."):
    print("Results for current directory:" + "\n" + f"Working Directory: {working_dir}" + "\n" + f"Directory: {directory}" + "\n" + get_files_info(working_dir, directory)) 

test_list = [("calculator", "."), ("calculator", "pkg"), ("calculator", "/bin"), ("calculator", "../")]

for test_item in test_list:
    test(test_item[0], test_item[1])
    print("")
