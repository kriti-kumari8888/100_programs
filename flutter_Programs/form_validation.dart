import 'package:flutter/material.dart';

void main() => runApp(FormValidationDemo());

class FormValidationDemo extends StatelessWidget {
  @override
  Widget build(BuildContext context) => MaterialApp(home: FormPage());
}

class FormPage extends StatefulWidget {
  @override
  _FormPageState createState() => _FormPageState();
}

class _FormPageState extends State<FormPage> {
  final _formKey = GlobalKey<FormState>();
  String _name = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Form Validation')),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              TextFormField(
                decoration: InputDecoration(labelText: 'Name'),
                validator: (value) => (value == null || value.trim().isEmpty) ? 'Name required' : null,
                onSaved: (v) => _name = v ?? '',
              ),
              SizedBox(height: 16),
              ElevatedButton(
                child: Text('Submit'),
                onPressed: () {
                  if (_formKey.currentState?.validate() ?? false) {
                    _formKey.currentState?.save();
                    ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Hello, \\$_name')));
                  }
                },
              )
            ],
          ),
        ),
      ),
    );
  }
}
