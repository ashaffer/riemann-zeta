import RHBridge.P2RoundedFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FactorChunk3 :
    P2RoundedFactorCheckpointData.panel18Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18Prefix12_eq :
    P2RoundedFactorCheckpointData.panel18Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk3.1

theorem panel18Prefix13_eq :
    P2RoundedFactorCheckpointData.panel18Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk3.2.1

theorem panel18Prefix14_eq :
    P2RoundedFactorCheckpointData.panel18Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk3.2.2.1

theorem panel18Prefix15_eq :
    P2RoundedFactorCheckpointData.panel18Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk3.2.2.2

end RHP2Bridge
