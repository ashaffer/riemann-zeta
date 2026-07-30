import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel31FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel31FlatComponentChunk34

end RHP2Bridge
