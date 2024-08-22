@echo off
echo Ativando ambiente virtual...
call venv\Scripts\activate

echo Instalando dependências no diretório de build...
pip install -r requirements.txt -t build/

echo Copiando arquivos fonte para o diretório de build...
xcopy /E /I /Y src\* build\

echo Criando arquivo ZIP...
cd build
powershell Compress-Archive -Path * -DestinationPath ../deploy.zip
cd ..

echo Limpando diretório de build...
rd /s /q build

echo Arquivo deploy.zip criado com sucesso!
