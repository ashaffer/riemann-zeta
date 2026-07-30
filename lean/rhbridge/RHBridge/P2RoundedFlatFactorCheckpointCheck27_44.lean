import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk44 :
    P2RoundedFactorCheckpointData.panel27FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd20_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨20, by decide⟩ := by
  exact panel27FlatComponentChunk44

end RHP2Bridge
