package Mybank;

import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class Search implements ActionListener 
{
	DataInputStream din;
	DataOutputStream dout;
	String data[][]=new String[100][100];
	int i=0;
		
	private JFrame bank;
	private JFrame frms;
	private JPanel pnls;
	private JTextField tfs;
	private JButton bts;
	private String acc;
	private JFrame frmsd;
	private JPanel pnlsd;
	private JTextField tfacc;
	private JTextField tfn;
	private JTextField tfb;
	private JTextField tft;
	private JButton btsd;
	JLabel lb;

	public Search(JFrame frmacc, JLabel lb) 
	{
		// TODO Auto-generated constructor stub
	
		bank=frmacc;
		this.lb=lb;
		
		frms=new JFrame("Serach");
		frms.setSize(220,120);
		frms.setVisible(true);
		
		pnls=new JPanel(new FlowLayout());
		frms.add(pnls);
		pnls.add(new JLabel("Account No:"));
		tfs=new JTextField(8);
		pnls.add(tfs);
		
		bts=new JButton("Ok");
		pnls.add(bts);
		bts.addActionListener(this);
		lb.setText("Searching is Going on...");
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		Object obj = e.getSource();
		if(obj==bts)
		{
			fillArray();
			getData();
			display();
		}
		if(obj==btsd)
		{
			frmsd.dispose();
			frms.dispose();
			lb.setText("Searching is done.");
		}
		
	}

	private void display() {
		// TODO Auto-generated method stub
		frmsd=new JFrame("Display");
		frmsd.setSize(200,220);
		frmsd.setVisible(true);
		pnlsd=new JPanel(new FlowLayout());
		frmsd.add(pnlsd);
		pnlsd.add(new JLabel("Account No:"));
		tfacc=new JTextField(8);
		pnlsd.add(tfacc);
		
		pnlsd.add(new JLabel("Name:"));
		tfn=new JTextField(8);
		pnlsd.add(tfn);
		pnlsd.add(new JLabel("Balence:"));
		tfb=new JTextField(8);
		pnlsd.add(tfb);
		pnlsd.add(new JLabel("Type:"));
		tft=new JTextField(8);
		pnlsd.add(tft);

		btsd=new JButton("Ok");
		pnlsd.add(btsd);

		btsd.addActionListener(this);
		
		searchPerson();
	}

	private void searchPerson() {
		// TODO Auto-generated method stub
		
		int x=0,f=0;
		while(x<i)
		{
			if(data[x][0].equals(acc))
			{
				tfacc.setText(data[x][0]);
				tfn.setText(data[x][1]);
				tfb.setText(data[x][2]);
				tft.setText(data[x][3]);
				f=1;
			}
		
			x++;
		}
		
		if(f==0)
		{
			JOptionPane.showMessageDialog(bank, "Account No is not Present");
		}
	}

	private void getData() {
		// TODO Auto-generated method stub
		acc=tfs.getText();
	}

	private void fillArray() {
		// TODO Auto-generated method stub
		Boolean eof=false;

		try {
			din=new DataInputStream(new FileInputStream("BankSystem.txt"));

			while(!eof)
			{
				try{
					while(true)
					{
						for(int j=0;j<=3;j++)
						{
							data[i][j]=din.readUTF();
						}
						i++;
					}

				}catch(EOFException e)
				{
					eof=true;
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}

			try {
				din.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}


	}

}
