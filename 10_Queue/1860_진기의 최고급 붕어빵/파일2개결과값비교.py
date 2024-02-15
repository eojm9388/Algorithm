def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # 파일 내용을 읽어와서 비교
        content1 = f1.readlines()
        content2 = f2.readlines()

        # 두 파일 내용이 일치하는지 확인
        diff_count = 0
        for line1, line2 in zip(content1, content2):
            if line1 != line2:
                print(f"첫 번째 파일: {line1.strip()}")
                print(f"두 번째 파일: {line2.strip()}")
                print()
                diff_count += 1

        if diff_count == 0:
            print("두 파일은 완전히 일치합니다.")
        else:
            print("두 파일은 일치하지 않습니다.")


file1_path = "out1.txt"
file2_path = "out2.txt"

compare_files(file1_path, file2_path)
