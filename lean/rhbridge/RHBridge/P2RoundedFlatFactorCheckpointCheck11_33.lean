import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel11FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel11FlatComponentChunk33

end RHP2Bridge
