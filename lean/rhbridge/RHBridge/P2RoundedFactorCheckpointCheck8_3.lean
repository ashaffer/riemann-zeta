import RHBridge.P2RoundedFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FactorChunk3 :
    P2RoundedFactorCheckpointData.panel8Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨8, by decide⟩ := by
  decide +kernel

theorem panel8Prefix12_eq :
    P2RoundedFactorCheckpointData.panel8Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk3.1

theorem panel8Prefix13_eq :
    P2RoundedFactorCheckpointData.panel8Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk3.2.1

theorem panel8Prefix14_eq :
    P2RoundedFactorCheckpointData.panel8Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk3.2.2.1

theorem panel8Prefix15_eq :
    P2RoundedFactorCheckpointData.panel8Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk3.2.2.2

end RHP2Bridge
