import os, subprocess

TEST_DIR  ="/tests"
CODE_FILE = "main.c"
COMPILER_TIMEOUT = 10.0

code_path= os.path.join(TEST_DIR,CODE_FILE)
app_path = os.path.join(TEST_DIR,"app")

print("building ...")
try:    
        ret = subprocess.run(["gcc", code_path,"-o",app_path],
                stdout =subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=COMPILER_TIMEOUT)
        
except Exception as e:
        print("error: compilation faild.",str(e))
        exit(1)
 
output = ret.stdout.decode("utf-8")
print(output)
output = ret.stderr.decode("utf-8")
print(output)

if ret.returncode != 0:
        print("compilation failed")
        exit(1)

print("running ...")
try:    
        ret = subprocess.run([app_path],
                stdout =subprocess.PIPE,
                timeout=COMPILER_TIMEOUT)
        
except Exception as e:
        print("error: runtime faild.",str(e))
        exit(1)

output = ret.stdout.decode("utf-8")
print(output)
print("all test are passed")
exit(0)