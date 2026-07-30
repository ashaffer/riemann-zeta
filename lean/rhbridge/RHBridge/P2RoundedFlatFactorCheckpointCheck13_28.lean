import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel13FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel13FlatComponentChunk28

end RHP2Bridge
