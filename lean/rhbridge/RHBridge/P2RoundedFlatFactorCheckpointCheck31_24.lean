import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel31FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel31FlatComponentChunk24

end RHP2Bridge
