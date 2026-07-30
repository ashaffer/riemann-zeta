import RHBridge.P2RoundedFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FactorChunk1 :
    P2RoundedFactorCheckpointData.panel8Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨8, by decide⟩ := by
  decide +kernel

theorem panel8Prefix4_eq :
    P2RoundedFactorCheckpointData.panel8Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk1.1

theorem panel8Prefix5_eq :
    P2RoundedFactorCheckpointData.panel8Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk1.2.1

theorem panel8Prefix6_eq :
    P2RoundedFactorCheckpointData.panel8Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk1.2.2.1

theorem panel8Prefix7_eq :
    P2RoundedFactorCheckpointData.panel8Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk1.2.2.2

end RHP2Bridge
