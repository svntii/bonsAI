import React, { useState } from 'react';
import { Text, View, TouchableOpacity, Dimensions } from 'react-native';
import { Icon } from '@rneui/themed';


const Header: React.FC = () => {
    const [isExpanded, setIsExpanded] = useState(false);

    const handleToggle = () => {
        setIsExpanded(!isExpanded);
    };

    const windowHeight = Dimensions.get('window').height;
    return (
        <TouchableOpacity
            onPress={handleToggle}
        >
            <View style={{
                position: 'absolute',
                top: 0,
                width: '100%',
                height: isExpanded ? windowHeight : 50,
                backgroundColor: 'lightblue',
                zIndex: 9999,
                alignItems: 'center',
            }}
            >
                <Icon
                    name="forward"
                />                
                            
            </View>
        </TouchableOpacity>
    );
};

export default Header;