import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel11FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel11FlatComponentChunk25

end RHP2Bridge
