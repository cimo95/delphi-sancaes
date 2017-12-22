object Form1: TForm1
  Left = 381
  Top = 180
  BorderIcons = [biSystemMenu]
  BorderStyle = bsSingle
  Caption = 'Sancaes 1.0'
  ClientHeight = 360
  ClientWidth = 663
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'segoe ui'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 200
    Top = 331
    Width = 270
    Height = 13
    Caption = 'Shift count :             (0 = as long as password length)'
  end
  object Label2: TLabel
    Left = 8
    Top = 331
    Width = 58
    Height = 13
    Caption = 'Password : '
  end
  object Memo1: TMemo
    Left = 8
    Top = 8
    Width = 649
    Height = 153
    Font.Charset = ANSI_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Courier New'
    Font.Style = []
    ParentFont = False
    ScrollBars = ssVertical
    TabOrder = 0
    WordWrap = False
  end
  object Memo2: TMemo
    Left = 8
    Top = 168
    Width = 649
    Height = 153
    Font.Charset = ANSI_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Courier New'
    Font.Style = []
    ParentFont = False
    ScrollBars = ssVertical
    TabOrder = 1
    WordWrap = False
  end
  object Button1: TButton
    Left = 496
    Top = 328
    Width = 35
    Height = 25
    Caption = 'ENC'
    TabOrder = 2
    OnClick = Button1Click
  end
  object Button2: TButton
    Left = 534
    Top = 328
    Width = 35
    Height = 25
    Caption = 'DEC'
    TabOrder = 3
    OnClick = Button2Click
  end
  object Edit1: TEdit
    Left = 272
    Top = 328
    Width = 25
    Height = 21
    TabOrder = 4
    Text = '0'
    OnChange = Edit1Change
    OnKeyPress = Edit1KeyPress
  end
  object Edit2: TEdit
    Left = 64
    Top = 328
    Width = 121
    Height = 21
    PasswordChar = 'x'
    TabOrder = 5
  end
  object Button3: TButton
    Left = 574
    Top = 328
    Width = 35
    Height = 25
    Caption = 'MOV'
    TabOrder = 6
    OnClick = Button3Click
  end
  object Button4: TButton
    Left = 614
    Top = 328
    Width = 35
    Height = 25
    Caption = 'WW'
    TabOrder = 7
    OnClick = Button4Click
  end
end
