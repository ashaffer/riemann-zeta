import RHBridge.P2RoundedFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FactorChunk1 :
    P2RoundedFactorCheckpointData.panel24Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨24, by decide⟩ := by
  decide +kernel

theorem panel24Prefix4_eq :
    P2RoundedFactorCheckpointData.panel24Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk1.1

theorem panel24Prefix5_eq :
    P2RoundedFactorCheckpointData.panel24Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk1.2.1

theorem panel24Prefix6_eq :
    P2RoundedFactorCheckpointData.panel24Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk1.2.2.1

theorem panel24Prefix7_eq :
    P2RoundedFactorCheckpointData.panel24Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk1.2.2.2

end RHP2Bridge
