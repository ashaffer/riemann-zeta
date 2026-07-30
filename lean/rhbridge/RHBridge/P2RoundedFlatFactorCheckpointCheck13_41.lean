import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel13FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel13FlatComponentChunk41

end RHP2Bridge
