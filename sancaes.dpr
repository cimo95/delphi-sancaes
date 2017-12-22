program sancaes;

uses
  Forms,
  uutama in 'uutama.pas' {Form1},
  usancaes in 'usancaes.pas';

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TForm1, Form1);
  Application.Run;
end.
