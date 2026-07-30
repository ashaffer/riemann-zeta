import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel31FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel31FlatComponentChunk26

end RHP2Bridge
