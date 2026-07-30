import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel31FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel31FlatComponentChunk25

end RHP2Bridge
