import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel11FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel11FlatComponentChunk26

end RHP2Bridge
