import 'package:flutter/material.dart';

void main() => runApp(ListViewDemo());

class ListViewDemo extends StatelessWidget {
  final List<String> items = List.generate(20, (i) => 'Item \\${i + 1}');

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ListView Demo',
      home: Scaffold(
        appBar: AppBar(title: Text('ListView Demo')),
        body: ListView.separated(
          itemCount: items.length,
          separatorBuilder: (_, __) => Divider(),
          itemBuilder: (context, index) => ListTile(
            title: Text(items[index]),
            leading: CircleAvatar(child: Text('\\${index + 1}')),
          ),
        ),
      ),
    );
  }
}
