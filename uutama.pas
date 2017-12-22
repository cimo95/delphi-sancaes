Unit uutama;

Interface

Uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ShellAPI, FileCtrl, XPMan, usancaes, StdCtrls;

Type
  TForm1 = Class(TForm)
    Memo1: TMemo;
    Memo2: TMemo;
    Button1: TButton;
    Button2: TButton;
    Label1: TLabel;
    Edit1: TEdit;
    Label2: TLabel;
    Edit2: TEdit;
    Button3: TButton;
    Button4: TButton;
    Procedure Button1Click(Sender: TObject);
    Procedure Button2Click(Sender: TObject);
    Procedure Edit1KeyPress(Sender: TObject; Var Key: Char);
    Procedure Edit1Change(Sender: TObject);
    Procedure Button3Click(Sender: TObject);
    Procedure Button4Click(Sender: TObject);
  Private
    { Deklarasi hanya untuk penggunaan dalam unit ini saja }
  Public
    { Deklarasi untuk penggunaan ke semua unit yang terintegerasi }
  End;

Var
  Form1: TForm1;

Implementation

{$R *.dfm} //template tweaked by : Araachmadi Putra Pambudi

Procedure TForm1.Button1Click(Sender: TObject);
Begin
  If Length(Edit2.Text) = 0 Then
    Exit
  Else
    Memo2.Text := sEncryptText(Memo1.Text, Edit2.Text, StrToInt(Edit1.Text));
End;

Procedure TForm1.Button2Click(Sender: TObject);
Begin
  If Length(Edit2.Text) = 0 Then
    Exit
  Else
    Memo2.Text := sDecryptText(Memo1.Text, Edit2.Text, StrToInt(Edit1.Text));
End;

Procedure TForm1.Edit1KeyPress(Sender: TObject; Var Key: Char);
Begin
  If Not (Key In ['0'..'9', #8]) Then
    Key := #0;
End;

Procedure TForm1.Edit1Change(Sender: TObject);
Begin
  If Length(Edit1.Text) < 1 Then
    Edit1.Text := '0';
End;

Procedure TForm1.Button3Click(Sender: TObject);
Begin
  Memo1.Text := Memo2.Text;
  Memo2.Clear;
End;

Procedure TForm1.Button4Click(Sender: TObject);
Begin
  Memo1.WordWrap := Not Memo1.WordWrap;
  Memo2.WordWrap := Not Memo2.WordWrap;
End;

End.

