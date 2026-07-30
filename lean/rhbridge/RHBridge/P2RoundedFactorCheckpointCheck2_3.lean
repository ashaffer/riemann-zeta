import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk3 :
    P2RoundedFactorCheckpointData.panel2Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Prefix12_eq :
    P2RoundedFactorCheckpointData.panel2Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk3.1

theorem panel2Prefix13_eq :
    P2RoundedFactorCheckpointData.panel2Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk3.2.1

theorem panel2Prefix14_eq :
    P2RoundedFactorCheckpointData.panel2Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk3.2.2.1

theorem panel2Prefix15_eq :
    P2RoundedFactorCheckpointData.panel2Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk3.2.2.2

end RHP2Bridge
