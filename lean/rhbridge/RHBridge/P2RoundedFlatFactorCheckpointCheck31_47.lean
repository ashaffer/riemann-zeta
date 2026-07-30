import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel31FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel31FlatComponentChunk47

end RHP2Bridge
