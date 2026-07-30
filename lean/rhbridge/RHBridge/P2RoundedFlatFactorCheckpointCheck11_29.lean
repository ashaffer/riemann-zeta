import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel11FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel11FlatComponentChunk29

end RHP2Bridge
