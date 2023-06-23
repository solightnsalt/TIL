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

  

+ 정상작동 시 terminal msg

```bash
solda@SOL-home MINGW64 ~/Desktop/dev/GIT/TIL/React (main)
$ yarn create react-app week-1
➤ YN0000: ┌ Resolution step
➤ YN0061: │ tar@npm:2.2.2 is deprecated: This version of tar is no longer supported, and will not receive s
ecurity updates. Please upgrade asap.
➤ YN0000: └ Completed in 1s 405ms
➤ YN0000: ┌ Fetch step
➤ YN0000: └ Completed
➤ YN0000: ┌ Link step
➤ YN0000: └ Completed
➤ YN0000: Done with warnings in 1s 566ms


Creating a new React app in C:\Users\solda\Desktop\dev\GIT\TIL\React\week-1.

Installing packages. This might take a couple of minutes.
Installing react, react-dom, and react-scripts with cra-template...

➤ YN0000: ┌ Resolution step
➤ YN0032: │ fsevents@npm:2.3.2: Implicit dependencies on node-gyp are discouraged
➤ YN0061: │ svgo@npm:1.3.2 is deprecated: This SVGO version is no longer supported. Upgrade to v2.x.x.     
➤ YN0061: │ workbox-cacheable-response@npm:6.6.0 is deprecated: workbox-background-sync@6.6.0
➤ YN0061: │ rollup-plugin-terser@npm:7.0.2 is deprecated: This package has been deprecated and is no longer
 maintained. Please use @rollup/plugin-terser
➤ YN0061: │ stable@npm:0.1.8 is deprecated: Modern JS already guarantees Array#sort() is a stable sort, so 
this library is deprecated. See the compatibility table on MDN: https://developer.mozilla.org/en-US/docs/We
b/JavaScript/Reference/Global_Objects/Array/sort#browser_compatibility
➤ YN0061: │ w3c-hr-time@npm:1.0.2 is deprecated: Use your platform's native performance.now() and performan
ce.timeOrigin.
➤ YN0061: │ sourcemap-codec@npm:1.4.8 is deprecated: Please use @jridgewell/sourcemap-codec instead        
➤ YN0002: │ eslint-config-react-app@npm:7.0.1 [64b15] doesn't provide @babel/plugin-syntax-flow (p17639), r
equested by eslint-plugin-flowtype
➤ YN0002: │ eslint-config-react-app@npm:7.0.1 [64b15] doesn't provide @babel/plugin-transform-react-jsx (p4
66ce), requested by eslint-plugin-flowtype
➤ YN0000: │ Some peer dependencies are incorrectly met; run yarn explain peer-requirements <hash> for detai
ls, where <hash> is the six-letter p-prefixed code
➤ YN0000: └ Completed in 10s 423ms
➤ YN0000: ┌ Fetch step
➤ YN0013: │ yaml@npm:1.10.2 can't be found in the cache and will be fetched from the remote registry       
➤ YN0013: │ yaml@npm:2.3.1 can't be found in the cache and will be fetched from the remote registry        
➤ YN0013: │ yargs-parser@npm:20.2.9 can't be found in the cache and will be fetched from the remote regist 
➤ YN0013: │ yargs@npm:16.2.0 can't be found in the cache and will be fetched from the remote registry      
➤ YN0013: │ yocto-queue@npm:0.1.0 can't be found in the cache and will be fetched from the remote registry 
➤ YN0000: └ Completed in 11s 399ms
➤ YN0000: ┌ Link step
➤ YN0000: │ ESM support for PnP uses the experimental loader API and is therefore experimental
➤ YN0007: │ core-js@npm:3.31.0 must be built because it never has been before or the last one failed       
➤ YN0007: │ core-js-pure@npm:3.31.0 must be built because it never has been before or the last one failed  
➤ YN0000: └ Completed in 8s 831ms
➤ YN0000: Done with warnings in 30s 866ms

Installing template dependencies using yarnpkg...
➤ YN0000: ┌ Resolution step
➤ YN0002: │ eslint-config-react-app@npm:7.0.1 [64b15] doesn't provide @babel/plugin-syntax-flow (p17639), r
equested by eslint-plugin-flowtype
➤ YN0002: │ eslint-config-react-app@npm:7.0.1 [64b15] doesn't provide @babel/plugin-transform-react-jsx (p4
66ce), requested by eslint-plugin-flowtype
➤ YN0002: │ week-1@workspace:. doesn't provide @testing-library/dom (pcdd03), requested by @testing-library
/user-event
➤ YN0000: │ Some peer dependencies are incorrectly met; run yarn explain peer-requirements <hash> for detai
ls, where <hash> is the six-letter p-prefixed code
➤ YN0000: └ Completed in 3s 118ms
➤ YN0000: ┌ Fetch step
➤ YN0013: │ redent@npm:3.0.0 can't be found in the cache and will be fetched from the remote registry      
➤ YN0013: │ stop-iteration-iterator@npm:1.0.0 can't be found in the cache and will be fetched from the rem 
➤ YN0013: │ strip-indent@npm:3.0.0 can't be found in the cache and will be fetched from the remote registr 
➤ YN0013: │ web-vitals@npm:2.1.4 can't be found in the cache and will be fetched from the remote registry  
➤ YN0013: │ which-collection@npm:1.0.1 can't be found in the cache and will be fetched from the remote reg 
➤ YN0000: └ Completed in 1s 414ms
➤ YN0000: ┌ Link step
➤ YN0000: │ ESM support for PnP uses the experimental loader API and is therefore experimental
➤ YN0000: └ Completed in 0s 452ms
➤ YN0000: Done with warnings in 5s 199ms
Removing template package using yarnpkg...

➤ YN0000: ┌ Resolution step
➤ YN0002: │ eslint-config-react-app@npm:7.0.1 [64b15] doesn't provide @babel/plugin-syntax-flow (p17639), r
equested by eslint-plugin-flowtype
➤ YN0002: │ eslint-config-react-app@npm:7.0.1 [64b15] doesn't provide @babel/plugin-transform-react-jsx (p4
66ce), requested by eslint-plugin-flowtype
➤ YN0002: │ week-1@workspace:. doesn't provide @testing-library/dom (pcdd03), requested by @testing-library
/user-event
➤ YN0000: │ Some peer dependencies are incorrectly met; run yarn explain peer-requirements <hash> for detai
ls, where <hash> is the six-letter p-prefixed code
➤ YN0000: └ Completed in 0s 222ms
➤ YN0000: ┌ Fetch step
➤ YN0019: │ cra-template-npm-1.2.0-5ec02f7dcd-50f11eb15f.zip appears to be unused - removing
➤ YN0000: └ Completed in 0s 780ms
➤ YN0000: ┌ Link step
➤ YN0000: │ ESM support for PnP uses the experimental loader API and is therefore experimental
➤ YN0000: └ Completed in 0s 391ms
➤ YN0000: Done with warnings in 1s 610ms

Success! Created week-1 at C:\Users\solda\Desktop\dev\GIT\TIL\React\week-1
Inside that directory, you can run several commands:

  yarn start
    Starts the development server.

  yarn build
    Bundles the app into static files for production.

  yarn test
    Starts the test runner.

  yarn eject
    Removes this tool and copies build dependencies, configuration files
    and scripts into the app directory. If you do this, you can’t go back!

We suggest that you begin by typing:

  cd week-1
  yarn start

Happy hacking!
```



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

