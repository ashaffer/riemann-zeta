import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel31FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel31FlatComponentChunk31

end RHP2Bridge
