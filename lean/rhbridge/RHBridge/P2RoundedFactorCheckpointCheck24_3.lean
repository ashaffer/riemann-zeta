import RHBridge.P2RoundedFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FactorChunk3 :
    P2RoundedFactorCheckpointData.panel24Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨24, by decide⟩ := by
  decide +kernel

theorem panel24Prefix12_eq :
    P2RoundedFactorCheckpointData.panel24Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk3.1

theorem panel24Prefix13_eq :
    P2RoundedFactorCheckpointData.panel24Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk3.2.1

theorem panel24Prefix14_eq :
    P2RoundedFactorCheckpointData.panel24Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk3.2.2.1

theorem panel24Prefix15_eq :
    P2RoundedFactorCheckpointData.panel24Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk3.2.2.2

end RHP2Bridge
