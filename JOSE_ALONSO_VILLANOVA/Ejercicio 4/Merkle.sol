// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
    Este contrato es un ejemplo sencillo de cómo empezar
    a usar un Merkle Tree en Solidity.
    Está pensado como punto de partida (inicio de cadena),
    no como un sistema completo.
*/

contract DecisionChain {

    // Dirección del creador del contrato
    address public owner;

    // Raíz del Merkle Tree (hash principal)
    bytes32 public merkleRoot;

    // El constructor se ejecuta al desplegar el contrato
    constructor(bytes32 _merkleRoot) {
        owner = msg.sender;
        merkleRoot = _merkleRoot;
    }

    /*
        Modifier para que solo el owner pueda ejecutar
        ciertas funciones.
    */
    modifier onlyOwner() {
        require(msg.sender == owner, "No eres el propietario");
        _;
    }

    /*
        Permite cambiar la raíz del Merkle Tree.
        Esto simula el crecimiento de la cadena.
    */
    function updateMerkleRoot(bytes32 _newRoot) external onlyOwner {
        merkleRoot = _newRoot;
    }

    /*
        Esta función comprobaría si un elemento pertenece
        al Merkle Tree.
        
        De momento es un ejemplo base, sin librerías externas,
        para mostrar la estructura de decisión.
    */
    function verifyDecision(bytes32 _leaf) public pure returns (bool) {
        // Comprobación MUY simple (inicio del sistema)
        // En sistemas reales se usaría una prueba Merkle completa
        return _leaf != bytes32(0);
    }
}
