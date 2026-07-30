import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel31FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel31FlatComponentChunk27

end RHP2Bridge
