import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel13FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel13FlatComponentChunk25

end RHP2Bridge
