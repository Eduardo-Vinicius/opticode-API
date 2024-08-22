@echo off
echo Realizando deploy para o AWS Lambda...

set /p FUNCTION_NAME="Digite o nome da função Lambda: "

aws lambda update-function-code --function-name %FUNCTION_NAME% --zip-file fileb://deploy.zip

if %ERRORLEVEL% EQU 0 (
    echo Deploy realizado com sucesso!
) else (
    echo Erro no deploy. Verifique a saída para mais informações.
)
