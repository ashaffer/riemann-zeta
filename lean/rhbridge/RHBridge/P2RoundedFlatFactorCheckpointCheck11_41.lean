import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel11FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel11FlatComponentChunk41

end RHP2Bridge
