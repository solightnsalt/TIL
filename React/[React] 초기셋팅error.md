# react 초기설정 error log

## error 1

+ 상황

  `yarn create react-app week-1`로 새 프로젝트 생성 시 아래 오류 발생 

  *Usage Error: The nearest package directory (C:\Users\solda\Desktop\dev\GIT\TIL\React\week-1) doesn't seem to be part of the project declared in C:\Users\solda.*

```bash
solda@SOL-home MINGW64 ~/Desktop/dev/GIT/TIL/React (main)
$ yarn create react-app week-1
➤ YN0000: ┌ Resolution step
➤ YN0061: │ tar@npm:2.2.2 is deprecated: This version of tar is no longer supported, and will not receive s
ecurity updates. Please upgrade asap.
➤ YN0000: └ Completed in 0s 345ms
➤ YN0000: ┌ Fetch step
➤ YN0000: └ Completed
➤ YN0000: ┌ Link step
➤ YN0000: └ Completed
➤ YN0000: Done with warnings in 0s 507ms


Creating a new React app in C:\Users\solda\Desktop\dev\GIT\TIL\React\week-1.

Installing packages. This might take a couple of minutes.
Installing react, react-dom, and react-scripts with cra-template...

Usage Error: The nearest package directory (C:\Users\solda\Desktop\dev\GIT\TIL\React\week-1) doesn't seem to be part of the project declared in C:\Users\solda.

- If C:\Users\solda isn't intended to be a project, remove any yarn.lock and/or package.json file there.   
- If C:\Users\solda is intended to be a project, it might be that you forgot to list Desktop/dev/GIT/TIL/Re
act/week-1 in its workspace configuration.
- Finally, if C:\Users\solda is fine and you intend Desktop/dev/GIT/TIL/React/week-1 to be treated as a com
pletely separate project (not even a workspace), create an empty yarn.lock file in it.

$ yarn add [--json] [-E,--exact] [-T,--tilde] [-C,--caret] [-D,--dev] [-P,--peer] [-O,--optional] [--prefer
-dev] [-i,--interactive] [--cached] [--mode #0] ...

Aborting installation.
  yarnpkg add --exact react react-dom react-scripts cra-template --cwd C:\Users\solda\Desktop\dev\GIT\TIL\R
eact\week-1 has failed.

Deleting generated file... package.json
Deleting week-1/ from C:\Users\solda\Desktop\dev\GIT\TIL\React
Done.
```

+ 해결

  오류메세지에 나온 경로에 있던 `package.json` 파일 삭제 후 `create`명령어 재실행하니 정상적으로 프로젝트 생성됨🤩

  


## error 2

+ 상황

  프로젝트 생성 후 프로젝트 폴더 내에서 서버 실행 시 실행에는 성공했으나 과정 중 에러 한 건 발생 

  *ERROR in [eslint] Failed to load config "react-app" to extend from.*

```bash
solda@SOL-home MINGW64 ~/Desktop/dev/GIT/TIL/React/week-1 (main)
$ yarn start
(node:15832) [DEP_WEBPACK_DEV_SERVER_ON_AFTER_SETUP_MIDDLEWARE] DeprecationWarning: 'onAfterSetupMiddleware
' option is deprecated. Please use the 'setupMiddlewares' option.
(Use `node --trace-deprecation ...` to show where the warning was created)
(node:15832) [DEP_WEBPACK_DEV_SERVER_ON_BEFORE_SETUP_MIDDLEWARE] DeprecationWarning: 'onBeforeSetupMiddlewa
re' option is deprecated. Please use the 'setupMiddlewares' option.
Starting the development server...
Failed to compile.

[eslint] Failed to load config "react-app" to extend from.
Referenced from: C:\Users\solda\Desktop\dev\GIT\TIL\React\week-1\package.json
ERROR in [eslint] Failed to load config "react-app" to extend from.
Referenced from: C:\Users\solda\Desktop\dev\GIT\TIL\React\week-1\package.json

webpack compiled with 1 error
Compiled successfully!

You can now view week-1 in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://172.30.1.9:3000

Note that the development build is not optimized.
To create a production build, use yarn build.

webpack compiled successfully
Compiled successfully!

Compiled successfully!

  On Your Network:  http://172.30.1.9:3000
Note that the development build is not optimized.
To create a production build, use yarn build.

webpack compiled successfully
```

+ 해결

  `npm install eslint-config-react-app@6` 을 설치해주니 해당 오류 발생하지 않



[eslint]문법 교정 역할!  에서 말하는 규칙이 지켜지지 않았을 경우일 가능성

