import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel11FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel11FlatComponentChunk42

end RHP2Bridge
